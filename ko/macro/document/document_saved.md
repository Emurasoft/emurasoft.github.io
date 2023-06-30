# Saved 속성 (Document ��ü)

마지막으로 저장되거나 열린 후로 문서가 수정되었는지 여부를 나타내는 플래그를 검색하거나 설정합니다.

#### \[JavaScript\]

_bSaved_ = document. **Saved**;

document. **Saved** = _bSaved_;

#### \[VBScript\]

_bSaved_ = document. **Saved**

document. **Saved** = _bSaved_

## 예시

#### \[JavaScript\]

if( document.Saved )  alert( "The document is not changed." );

else  alert( "The document is changed." );

#### \[VBScript\]

If document.Saved Then

alert( "The document is not changed." )

Else

alert( "The document is changed." )

End If

## 버전

엠에디터 프로페셔널 버전 4.00 이상에서만 지원됩니다.