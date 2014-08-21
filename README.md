sublime-cssrtl
==============

## Processing directives

css-flip provides a way to ignore declarations or rules that should not be
flipped, and precisely replace property values.

### @noflip

Prevent a single declaration from being flipped.

单条不翻转:

```css
p {
  /*@noflip*/ float: left;
  clear: left;
}
```

生成如下代码:

```css
p {
  float: left;
  clear: right;
}
```



不翻转整个规则:

```css
/*@noflip*/
p {
  float: left;
  clear: left;
}
```

生成:

```css
p {
  float: left;
  clear: left;
}
```

### @replace

翻转的时候直接替换，见下面的例子

源代码:

```css
p {
  /*@replace: -32px -32px*/ background-position: -32px 0;
  /*@replace: ">"*/ content: "<";
}
```

生成:

```css
p {
  background-position: -32px -32px;
  content: ">";
}
```
