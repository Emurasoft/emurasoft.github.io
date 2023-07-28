# Configs Collection

Configs collection provides a collection of [**Config** objects](../config/index).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of configurations. |
| **[Item](item)** | Retrieves the [**Config** object](../config/index) for the configuration of the specified index. |

## Examples

### \[JavaScript\]

```
cfgs = new Enumerator( editor.Configs );
for( ; !cfgs.atEnd(); cfgs.moveNext() ){
cfg = cfgs.item();
alert( cfg.Name );
}
```

### \[VBScript\]

```
For Each cfg In editor.Configs
alert cfg.Name
Next
```

## Version

Supported on EmEditor Professional Version 7.00 or later.


```{toctree}
:maxdepth: 1
count
item
```
