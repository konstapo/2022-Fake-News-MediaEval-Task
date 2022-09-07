#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 * This file is part of the Multimedia Satellite Task 2018 at Media Eval.
 * The script is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * The script is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this script; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 * We kindly ask you to refer to the following publication in any publication
 * mentioning or employing this script:
 *
 * Benjamin Bischke, Patrick Helber, Zhengyu Zhao, Jens de Bruijn, Damian Borth:
 * The Multimedia Satellite Task at MediaEval 2018 - Emergency Response for
 * Flooding Events. In workshop proceedings of the MediaEval Workshop, Sophia
 * Antipolis, France (29-31 October 2018)
 *
 * Copyright statement:
 * ====================
 * (c) 2018 by Benjamin Bischke (benjamin.bischke@dfki.de)
 *  https://github.com/multimediaeval/2018-Multimedia-Satellite-Task,
 *  http://www.multimediaeval.org/mediaeval2018/
 *
 * Updated: 10.06.18, 18:03
"""

__author__ = "Benjamin Bischke"
__email__ = "Benjamin.Bischke@dfki.de"

"""
 * Updated: 31.07.2020, 10:40
 * For the Flood-Related Multimedia Task at MediaEval 2020
 * Edits made by Stelios Andreadis (ITI/CERTH) andreadisst@iti.gr
"""

from six import text_type
from multiprocessing.pool import Pool
from tqdm import *

import os
import sys
import json
import tweepy

try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2

""" 
    Please replace these strings with your custom access credentials.
    More details about how-to generate the access tokens can be found in the 
    official twitter documentation.
    https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens    
"""
ACCESS_TOKEN = u"YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = u"YOUR_ACCESS_TOKEN_SECRET"
CONSUMER_KEY = u"YOUR_CONSUMER_KEY"
CONSUMER_SECRET = u"YOUR_CONSUMER_SECRET"

def get_tweet_file_path(filepath_id_file, output_dir):
    """
    :param filepath_id_file: path to the file containing the tweet-ids
    :param output_dir: path to ouput dir
    :return: target path to the file in which the raw tweets should be stored
    """
    out_file_name = os.path.basename(filepath_id_file).replace("ids_",
                                                               "tweets_")
    out_file_path = os.path.join(output_dir, out_file_name)
    return out_file_path


def download_tweets_for_id_file(tweet_ids_file_path,
                                output_dir,
                                retry_count,
                                retry_delay
                                ):
    """
    :param tweet_ids_file_path: path to the file containing the tweet-ids
    :param tweet_file_path:
    :param retry_count: retry count for twitter api
    :param retry_delay: retry delay in seconds for the twitter api
    :return: None
    """

    def load_tweet_ids_from_file(file_path):
        with open(file_path, "r") as fp:
            tweet_ids = json.loads(fp.read())
        return tweet_ids

    def save_tweets_in_file(tweets, filepath):
        with open(filepath, "w") as fp:
            json.dump(tweets, fp)

    def get_twitter_api(retry_count, retry_delay):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth, retry_count=retry_count,
                          retry_delay=retry_delay, retry_errors=set([503]))

    def fetch_tweet_by_ids(retry_count, retry_delay, tweet_ids):
        api = get_twitter_api(retry_count, retry_delay)
        tweets = []
        sys.stdout.write("Downloading tweets:\n")
        with tqdm(total=int(len(tweet_ids)/100.)) as pbar_1:
            for i, idx in tqdm(enumerate(range(0, len(tweet_ids), 100))):
                res = tweet_ids[idx:idx + 100]
                pbar_1.update()
                try:
                    _tweets = api.statuses_lookup(res, tweet_mode='extended')
                except Exception as ex:
                    sys.stdout.write("Error while fetching Tweets! "
                                     "(%s, %s)\n" % (str(idx), ex.message))
                    continue
                tweets += [tweet._json for tweet in _tweets]
        return tweets

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    tweet_file_path = get_tweet_file_path(tweet_ids_file_path, output_dir)
    if not os.path.exists(tweet_file_path):
        tweet_ids = load_tweet_ids_from_file(tweet_ids_file_path)
        tweets = fetch_tweet_by_ids(retry_count, retry_delay, tweet_ids)
        save_tweets_in_file(tweets, tweet_file_path)


def download_image(args):
    try:
        url, image_path, tweet_id = args
        urlretrieve(url, image_path)
    except Exception as exp:
        sys.stdout.write("Error while downloading Image! Please check this tweet."
                         "(%s, %s)\n" % (str(tweet_id), exp))


def fetch_images(tweet_ids_file_path, output_dir, num_processes):
    """
    :param tweet_file: path to file in which the raw tweets are stored
    :param output_folder: output folder for images to be donwloaded
    :param num_processes: the number of processes used to download
            the images
    :return:
    """
    tweet_file_path = get_tweet_file_path(tweet_ids_file_path, output_dir)

    output_folder = os.path.join(output_dir, "images")
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    with open(tweet_file_path, "r") as fp:
        tweets = json.loads(fp.read())

    tweet_ids_with_urls = {t["id"]: t["entities"]["media"][0]["media_url"]
                           for t in tweets if "media" in t["entities"]}

    tweet_ids, file_paths, urls = [], [], []
    for tweet_id, url in tweet_ids_with_urls.items():
        img_file = os.path.join(output_folder, "%s.png" % (tweet_id))
        if not os.path.exists(img_file):
            file_paths.append(img_file)
            tweet_ids.append(tweet_id)
            urls.append(url)

    sys.stdout.write("Downloading images:\n")
    processes = Pool(processes=num_processes)
    with tqdm(total=len(urls)) as pbar_2:
        for i, _ in tqdm(enumerate(processes.imap(download_image,
                                   list(zip(urls, file_paths, tweet_ids))))):
            pbar_2.update()


def main(filepath_id_file,
         output_dir,
         retry_count,
         retry_delay,
         num_processes,
         ):
    download_tweets_for_id_file(filepath_id_file, output_dir, retry_count,
                                retry_delay)
    fetch_images(filepath_id_file, output_dir, num_processes)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '-f', '--path-to-id-file',
        default='.',
        type=text_type,
        help='specifies the path to the tweet-id file (the tweets to download)',
    )
    parser.add_argument(
        '-o', '--outdir',
        default='.',
        type=text_type,
        help='specifies the output directory in which tweets and embedded '
             'images will be downloaded',
    )
    parser.add_argument(
        '-rc', '--retry-count',
        default=10,
        type=int,
        help='specifies number of retries if rate limits or errors occur '
             'on the Twitter API ',
    )
    parser.add_argument(
        '-rd', '--retry-delay',
        default=5,
        type=int,
        help='seconds of to wait if rate limits or errors occur '
             'on the Twitter API ',
    )
    parser.add_argument(
        '-p', '--processes',
        default=4,
        type=int,
        help='specifies the number of processes used to download the images',
    )

    args, unknown = parser.parse_known_args()
    try:
        main(
            args.path_to_id_file,
            args.outdir,
            args.retry_count,
            args.retry_delay,
            args.processes,
        )
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("Done")
