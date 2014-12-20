sublime-cssrtl
==============
Generate CSS file from ltr to rtl

Generate CSS file from rtl to ltr

Usage Example：

![picture](https://github.com/junyuecao/private-static/blob/master/example.gif)

## Installation

### Install node module
```
npm install css-flip-auto -g
```

### Install sublime text plugin
1. From Package Control
2.Download (https://github.com/junyuecao/sublime-cssrtl/archive/master.zip)
unzip to the package folder of sublime text
 


## Exception

There are two types of exception - @noflip and @replace

### @noflip

#### exception for single css rule

From:

```css
p {
  /*@noflip*/ float: left;
  clear: left;
}
```

To:

```css
p {
  float: left;
  clear: right;
}
```



#### Entire css selector:

From: 

```css
/*@noflip*/
p {
  float: left;
  clear: left;
}
```

To:

```css
p {
  float: left;
  clear: left;
}
```

### @replace

Replace to custom rule.

From:

```css
p {
  /*@replace: -32px -32px*/ background-position: -32px 0;
  /*@replace: ">"*/ content: "<";
}
```

To:

```css
p {
  background-position: -32px -32px;
  content: ">";
}
```

## Support css attribute
  - background-position 
  - background-position-x\n border-bottom-left-radius
  - border-bottom-right-radius
  - border-color
  - border-left
  - border-left-color
  - border-left-style
  - border-left-width
  - border-radius
  - border-right
  - border-right-color
  - border-right-style
  - border-right-width
  - border-style
  - border-top-left-radius
  - border-top-right-radius
  - border-width
  - box-shadow
  - clear
  - direction
  - float
  - left
  - margin
  - margin-left
  - margin-right
  - padding
  - padding-left
  - padding-right
  - right
  - text-align 
  - transition 
  -transition-property


Thanks to： (https://github.com/twitter/css-flip)
