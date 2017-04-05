from datetime import date, timedelta

import requests


DEFAULT_DAYS_COUNT = 7
DEFAULT_REPS_NUMBER = 20
GITHUB_REP_API = 'https://api.github.com/search/repositories'


def get_date_some_days_ago(days_ago=DEFAULT_DAYS_COUNT):
    return str(date.today() - timedelta(days=days_ago))


def get_trending_repositories(reps_number, days_ago, API_url):
    period = get_date_some_days_ago(days_ago)
    request_params = {'q': 'created:>{}'.format(period),
                      'sort': 'stars',
                      'order': 'desc',
                      'per_page': str(reps_number)}
    all_repos = requests.get(API_url, request_params)
    return all_repos.json()['items']


def print_epositories_list(repositories):
    for index, rep in enumerate(repositories, 1):
        print('{}. Repository: {}\nURL: {}\nOpen issues: {}\n'.format
              (index,
               rep['full_name'].split('/')[1],
               rep['clone_url'],
               rep['open_issues']))


if __name__ == '__main__':
    repositories = get_trending_repositories(DEFAULT_REPS_NUMBER,
                                             DEFAULT_DAYS_COUNT,
                                             GITHUB_REP_API)
    print("The {} most popular repositories on github.com".format(DEFAULT_REPS_NUMBER))
    print_epositories_list(repositories)
