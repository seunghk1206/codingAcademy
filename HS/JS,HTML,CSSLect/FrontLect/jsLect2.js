var names = ['SKT', 'LG', 'Samsung']
var A = [11]
A = A.concat(names)
alert(A)
A.unshift('hi')
alert(A)
A.splice(2, 0, '111')
alert(A)
alert(A.slice(2, 4))

A.shift()
alert(A)
A.pop()
alert(A)
A.sort()
alert(A)
A.reverse()
alert(A)