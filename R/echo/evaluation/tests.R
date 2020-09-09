context({
  testcase("echo(\"test\")", {
    testEqual(NULL, function(env) { env$echo("test") }, 'test')
  })
  testcase("echo(\"test2\")", {
    testEqual(NULL, function(env) { env$echo("test2") }, 'test2')
  })
})
