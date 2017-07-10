# 数组


```javascript
var plavlist = [];

//  从0位置向数组添加元素
playList.unshift('1');

// 从后边添加元素
playList.push(1,44,55);

// 获取数组长度
playList.length;
```

# 语句

## if
```javascript
if ( condition ) {
// some action happens here
}

// 与
if (a > 1 && a < 10) {
//the value in a is between 1 and 10
alert("The value " + a + " is between 1 and 10");
}

// 或
if (key == 'n' || key == 'N') {
//move to the next photo
}

// 非
if (! valid) {
//print errors and don't submit form
}
```
- 比较操作符
``` javascript
== 
！=
===
!==
>
<
>=
<=

```
```

# loop
```javascript
while (condition) {
// javascript to repeat
}



for (var num = 1; num <= 100; num++) {
document.write('Number ' + num + ' <br>');
}
````

# 函数
```javascript
function functionName() {
// the JavaScript you want to run
}


function functionName(parameter1, parameter2, parameter3) {
// the JavaScript you want to run
}
```


# jQuery
```javascript
$(document).ready(function() {
// your programming goes here
});



$(function() {
// your programming goes here
}); // end ready

$('#selector').on('click', selector, myData, functionName);


$(‘ul’).on(‘click’, ‘li’, function() {
$(this).css(‘text-decoration’: ‘line-through’);
}); // end on

$('element').fadeOut('slow');

$('#message').animate(
{
left: '650px',
opacity: .5,
fontSize: '24px'
},
1500,
'linear'
);
```

Reboot-Ada 18:21:02




