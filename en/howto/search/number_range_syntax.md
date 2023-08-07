# Number Range Expression Syntax

EmEditor allows you to use number range expressions as search expressions.

To use a number range in **Find**, **Replace**, **Find in Files**, **Replace in Files**, or **Advanced Filter** dialog box select **Number Range** from the **Mode** drop-down list box.

To use a number range in **Find**, **Replace**, **FindInFiles**, **ReplaceInFiles**, or **Filter** methods of macros, include the **eeExFindNumberRange** flag to the **ExFlags** parameter.

A number range is expressed as an interval notation. A bracket indicates an included endpoint, and a parenthesis indicates an excluded endpoint. If both numbers do not
include a decimal point, the method matches only integers. Minimum and/or maximum number may be omitted to mean negative and/or positive infinity. The number format depends on the locale specified in the **Locale** drop-down list box in the [**Sort** page](../../dlg/customize/sort/index) of the **Customize** dialog box. In some locales (such as German), a comma (',') is used to denote a decimal point, and in that case, a space before and after the separator comma is necessary to avoid ambiguity.

As of v19.6, a number range can specify a set of numbers with a specified increment. An increment can be specified as the third parameter "c" in \[a , b , c\] or (a , b , c).

For instance,

| Number Range | Meaning |
| --- | --- |
| \[1 , 9\] | matches integers 1, 2, 3, ..., 9. |
| \[ , 9) | matches any integers less than 9. |
| \[1.0 , 9.0) | matches decimal numbers greater than or equal to 1.0, and less than 9.0. |
| \[ , 1.0) | matches any decimal numbers less than 1.0 |
| (2.0 , \] | matches any decimal number greater than 2.0 |
| \[1,0 , 9,0 "," \] | matches decimal numbers greater than or equal to 1.0, and less than 9.0 using a comma as a decimal point. |
| \[1 , 9 , 2\] | matches integers 1, 3, 5, 7, 9. |
| \[1.0.0.0 , 1.255.255.255\] | matches IPv4 addresses 1.0.0.0 ... 1.255.255.255. |
| 1.1.1.1/8 | matches IPv4 addresses 1.0.0.0 ... 1.255.255.255. |
| 2001:db8::/48 | matches IPv6 addresses 2001:db8:: ... 2001:db8:0:ffff:ffff:ffff:ffff:ffff. |
| \[1/1/2021 , 12/31/2022\] | matches dates 1/1/2021 ... 12/31/2022. |
| \[1/1/2021 , 12/31/2022 "M/d/yyyy" \] | matches dates 1/1/2021 ... 12/31/2022 using the "M/d/yyyy" format. |
| \[13:00:00 , 18:59:59 "HH:mm:ss" \] | matches times 13:00:00 ... 18:59:59 using the "HH:mm:ss" format. |
| \[2021-01-01 00:00:00 , 2022-12-31 23:59:59 "yyyy-MM-dd HH:mm:ss" \] | matches dates and times 2021-01-01 00:00:00<br> ... 2022-12-31 23:59:59 using the "yyyy-MM-dd HH:mm:ss" format. |

## Date and Time formats

The following formats can be used to make date and/or time formats.

| Format | Meaning |
| --- | --- |
| yy | Year represented only by the last two digits. |
| yyyy | Year represented by four digits. |
| M | Month as digits without leading zeros for single-digit months. |
| MM | Month as digits with leading zeros for single-digit months. |
| MMM | Abbreviated month name, for example, "Nov" in English. This format may not be available if the current locale does not provide month names. |
<!-- cspell:disable-next-line -->
| MMMM | Month name, for example, "November" for English, and "Noviembre" for Spanish. This format may not be available if the current locale does not provide month names. |
| d | Day of the month as digits without leading zeros for single-digit days. |
| dd | Day of the month as digits with leading zeros for single-digit days. |
| HH:mm | Hours and minutes separated by a colon; 24-hour clock. |
| HH:mm:ss | Hours, minutes and seconds separated by a colon; 24-hour clock. |
| \| | Or. Use this to combine multiple formats, allowing the number range expression to match either formats. |

## See Also

- [Replacement Expression Syntax](replacement_expression_syntax)
