
context({
  testcase('The correct method was used', {
    testEqual("test$alternative", function(env) { env$test$alternative }, 'two.sided')
    testEqual("test$method", function(env) { env$test$method }, ' Two Sample t-test')
  })
  testcase('p value is correct', {
    testEqual("test$p.value", function(env) { env$test$p.value }, 0.1753, tolerance = 1e-3)
  })
}, preExec = {
  set.seed(20190322)
})

context({
  testcase('y has the correct length', {
    testEqual("length(y)", function(env) { length(env$y) }, 100)
  })
})