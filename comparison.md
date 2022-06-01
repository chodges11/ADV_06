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
       *   Relational - 
       *   MongoDB - 

    * Add a status update.
       *   Relational - 
       *   MongoDB - 

    * Update a user update.
       *   Relational - 
       *   MongoDB - 

    * Update a status update.
       *   Relational - 
       *   MongoDB - 

    * Search for a user update.
       *   Relational - 
       *   MongoDB -

    * Search for a status update.
       *   Relational - 
       *   MongoDB - 

    * Delete a user update.
       *   Relational - 
       *   MongoDB -

    * Delete a status update.
       *   Relational - 
       *   MongoDB - 

## Recommendation

A couple of things stand out right away. Firstly, The Relational DB does not
have the extra files of user.py and user_status.py. I would have done away with
them, in the MongoDB instance, if I had more time. So It's not a perfect apples
to apples comparison, but that may be a negligible amount of extra time. Maybe
you can tell me.

Secondly, clearly I did not implement the MongoDB load Status updates in the
most optimized fashion. So I'm not convinced that those are fair comparisons
either.

