# HISTORY\_INFO

蚚衾 [EVENT\_HISTORY 奀潔](../event/index) 笢﹝

```
typedef struct _HISTORY_INFO {
	size_t cbSize;
	UINT nFlags;
	POINT_PTR ptTop;
	POINT_PTR ptBottom;
	UINT nChar;
	LPCWSTR pszString;
} HISTORY_INFO;
```

## 凳傖

_cbSize_

眕趼誹峈等弇腔杅擂賦凳湮苤﹝婓諉彶 EVENT\_HISTORY 眳ゴㄛ參蜆傖埜扢峈 sizeof( HISTORY\_INFO )﹝

_nFlags_

硌隅珨跺狟蹈硉腔郪磁﹝

|     |     |
| --- | --- |
| HISTORY\_INSERT\_CHAR | 脣⻌賸珨跺趼睫﹝ |
| HISTORY\_BACK\_SPACE | 偌賸綴豖瑩懂痄壺趼睫﹝ |
| HISTORY\_DELETE\_CHAR | 偌狟刉壺瑩懂痄壺趼睫﹝ |
| HISTORY\_INSERT\_STRING | 脣⻌賸珨跺趼睫揹﹝ |
| HISTORY\_DELETE\_STRING | 刉壺賸珨跺趼睫揹﹝ |
| HISTORY\_INSERT\_TAB\_SEL | 偌賸 Tab 瑩懂坫輛恁Е﹝ |
| HISTORY\_MODIFIED | 恅紫掩党蜊﹝ |
| HISTORY\_COMBINED | 盪妢暮翹岈璃茼迵載婌眳ゴ腔岈璃磁甜﹝ |
| HISTORY\_CR\_ONLY | 掩痄壺腔趼睫岆躺 CR﹝ |
| HISTORY\_LF\_ONLY | 掩痄壺腔趼睫岆躺 LF﹝ |
| HISTORY\_SEL\_BOX | 脣⻌腔趼睫揹岆珨跺晶眻恁龰﹝ |
| HISTORY\_INSIDE\_UNDO | 蜆紱釬掩婦漪婓雪秏韜鍔爵﹝ |
| HISTORY\_INSIDE\_REDO | 蜆紱釬掩婦漪婓笭酕韜鍔爵﹝ |

_ptTop_

涴跺傖埜婦漪眳ゴ腔嫖梓弇离﹝⺼彆 nFlags 傖埜婦漪 HISTORY\_INSERT\_STRINGㄛ涴跺傖埜岆恁Е腔お宎弇离﹝

_ptBottom_

⺼彆 nFlags 傖埜婦漪 HISTORY\_INSERT\_STRINGㄛ饒繫蜆傖埜岆恁Е腔賦帣弇离﹝祥�ㄛ綺謹涴跺傖埜﹝

_nChar_

⺼彆 nFlags 婦漪 HISTORY\_BACK\_SPACE 麼 HISTORY\_DELETE\_CHARㄛ涴跺傖埜婦漪掩痄壺腔趼睫﹝

_pszString_

⺼彆 nFlags 傖埜婦漪 HISTORY\_DELETE\_STRINGㄛ蜆傖埜婦漪掩痄壺腔趼睫揹﹝

## 盓厥唳掛

盓厥 EmEditor 9.00 麼眳綴腔唳掛﹝
