sublime-cssrtl
==============
## 安装

### 安装node依赖插件
```
npm install css-flip-auto -g
```

### 安装sublime 插件
下载(https://github.com/junyuecao/sublime-cssrtl/archive/master.zip)
解压缩到 sublime 的package目录中
 


## 处理方法

主要有两种方式来做非常规的翻转 @noflip 和@replace

### @noflip

防止单条规则的翻转

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



不翻转整个选择器:

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

## 支持的属性
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
