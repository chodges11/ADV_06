# Assignment 06 - Charles Hodges
# Database Performance Comparison Report

## Results

    * Load user database from a CSV file.
       *   Relational - Elapsed time: 0.3656 seconds
       *   MongoDB - Elapsed time: 0.9418 seconds

    * Load status database from a CSV file.
       *   Relational - Elapsed time: 39.2789 seconds
       *   MongoDB - Elapsed time: 152.1995 seconds

    * Add a user update.
       *   Relational - Elapsed time: 0.0074 seconds
       *   MongoDB - Elapsed time: 0.0021 seconds

    * Add a status update.
       *   Relational - Elapsed time: 0.0072 seconds
       *   MongoDB - Elapsed time: 0.0014 seconds

    * Update a user update.
       *   Relational - Elapsed time: 0.0071 seconds
       *   MongoDB - Elapsed time: 0.0049 seconds

    * Update a status update.
       *   Relational - Elapsed time: 0.0068 seconds
       *   MongoDB - Elapsed time: 0.0022 seconds

    * Search for a user update.
       *   Relational - Elapsed time: 0.0018 seconds
       *   MongoDB - Elapsed time: 0.0022 seconds

    * Search for a status update.
       *   Relational - Elapsed time: 0.0014 seconds
       *   MongoDB - Elapsed time: 0.0020 seconds

    * Delete a user update.
       *   Relational - Elapsed time: 0.0082 seconds
       *   MongoDB - Elapsed time: 0.0029 seconds

    * Delete a status update.
       *   Relational - Elapsed time: 0.0070 seconds
       *   MongoDB - Elapsed time: 0.0034 seconds

## Recommendation

Timer code used:

    * https://realpython.com/python-timer/
    * https://pypi.org/project/codetiming/

A couple of things stand out right away. Firstly, The Relational DB does not
have the extra files of user.py and user_status.py. I would have done away with
them, in the MongoDB instance, if I had more time. So It's not a perfect apples
to apples comparison, but that may be a negligible amount of extra time. Maybe
you can tell me.

Secondly, clearly I did not implement the MongoDB load Status updates in the
most optimized fashion. So I'm not convinced that those are fair comparisons
either.

In the general comparison, Relational was generally a smidge faster in
searching, for both Users and Statuses. And not including Loading, generally
MongoDB was a half or even a third of the elapsed time of the Relational DB.

In the end, I would recommend the MongoDB implementation, since it was
demonstrably faster in all areas, comparable in Search, and I believe that
loading times could likely be optimized and improved.