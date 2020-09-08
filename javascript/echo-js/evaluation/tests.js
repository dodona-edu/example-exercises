judge.config('switch-tab', 'echo');
judge.test('echo(5);', 5);
judge.test('echo(4);', 4);
judge.test('echo("4");', "4");
judge.test('echo(true);', true);
judge.test('echo("Twinkle, twinkle, little star,\\nHow I wonder what you are!\\nUp above the world so high,\\nLike a diamond in the sky.");', "Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.");
