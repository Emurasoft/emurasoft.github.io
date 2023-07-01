# Difference between Batch Replace All and Bulk Replace All

**Batch Replace All** searches a whole document for one string at a time, and repeats this procedure for the number of search strings. **Bulk Replace All** searches for all search strings simultaneously. The difference may lead to different results if search/replace string pairs contain, for instance:

1 → 5

2 → 4

4 → 2

5 → 1

and if the source document is:

\[1,2,3,4,5\]

In this case, if **Batch Replace All** is used, EmEditor will replace 1 with 5 for the whole document first, and then will replace 2 with 4. At this point, the source document becomes:

\[5,4,3,4,5\]

Next, when it replaces 4 with 2, note that it will replace two 4's (the second and fourth numbers). Lastly, when it replaces 5 with 1, it will replace two 5's (the first and last numbers). Thus, the result will be:

\[1,2,3,2,1\]

If the new **Bulk Replace All** is used, EmEditor will replace all strings simultaneously. Therefore, the result will be:

\[5,4,3,2,1\]

as you expect.

**Bulk Replace All** will replace much faster than **Batch Replace All**. In our test, **Bulk Replace All** completed 6310 times faster than **Batch Replace All** when one million search/replace pairs existed (See [Version 21.7](../../history/v21_7) for test results).

**Bulk Replace All** does not support regular expressions, number ranges, or strings including newlines.
