namespace MyFirstConsoleApp.Tests
{
  using NUnit.Framework;
  using ExampleExercises;

  using System;
  using System.IO;

  [TestFixture]
  public class Tests1
  {

    [TestCaseStd("Hello world!")]
    [TestCaseStd("Hello Dodona!")]
    public void SimpleTest(string InputString)
    {
      var expectedResult = InputString + "\n";

      var stringReader = new StringReader(InputString);
      Console.SetIn(stringReader);
      var stringWriter = new StringWriter();
      Console.SetOut(stringWriter);

      Echo.Main(new String[0]);
      Assert.AreEqual(expectedResult, stringWriter.ToString());
    }

  }
}
