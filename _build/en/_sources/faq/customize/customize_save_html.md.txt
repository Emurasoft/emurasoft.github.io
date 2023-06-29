# Q. Can EmEditor encode Unicode characters as "Numerical Character References" (NCRs - those &\#xxx; codes) when saving HTML or XML files?

Yes. On the **File** tab in **Properties**, click **Saving** button, and check
**Save Unicode as HTML/XML Character Reference**. You can also click **Use Named**
**Entity Reference** if you would like to save named entity references such as
"&copy;". For HTML and XML configurations, these checkboxes are checked by default.
However, EmEditor currently cannot decode or display NCRs as real Unicode
characters when loading HTML or XML files.