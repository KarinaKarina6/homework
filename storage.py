# -*- coding: utf-8 -*-
import datetime


BLOG_ENTRIES = [
    {
        'key': 'some_id',
        'title': 'It\'s first entry',
        'text': """The term normalisation comes from the database world. It refers to transforming the schema of a 
        database to remove redundant information. Also, redundant information means the same data that is stored in more 
        than one place.""",
        'created_at': datetime.datetime.now(),
        'comments': [
            {
                'name': 'Julius Koronci',
                'text': 'Nice article'
            },
            {
                'name': 'Alexander Shirokov',
                'text': 'Thanks for good article'
            }
        ]
    },
{
        'key': '1',
        'title': 'It\'s second entry',
        'text': """Recommender systems are software tools and techniques providing suggestions for
items to be of use to a user. The suggestions provided by a recommender system are
aimed at supporting their users in various decision-making processes, such as what
items to buy, what music to listen, or what news to read.""",
        'created_at': datetime.datetime.now(),
        'comments': [
            {
                'name': 'Francesco Ricci',
                'text': 'This is my article!'
            }
        ]
    }
]
