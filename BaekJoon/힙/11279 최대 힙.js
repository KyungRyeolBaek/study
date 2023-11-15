const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number)

input.shift()
const answer = []
let res = ''

input.map((n, i) => {
  if(n[i] === 0) {
    if(answer.length > 0) {
      const maxVal = answer.map(n => Math.max(n))
      res = maxVal
      answer.splice(answer.findIndex(maxVal))
    } else {
      res = 0
    }
  } else {
    answer.push(n)
  }
    console.log(res+'\n')    
})
