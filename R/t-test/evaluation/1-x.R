context({
  testcase('x has the correct length', {
    testEqual("length(x)", function(env) { length(env$x) }, 100)
  })
})