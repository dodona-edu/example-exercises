// hulpfunctie om oplossingen van methoden suggereren en invullen te testen
function checkMadLibs(expected, generated, madlib, categories) {
    
	// stringmethode om na te gaan of string enkel uit hoofdletters bestaat
	function isUpperCase(s) {
	    return s.search(/^[A-Z]+$/) === 0;
	};

	// stringmethode om na te gaan of string bestaat uit hoofdletter gevolgd door 
	// kleine letters
	function isCapitalized(s) {
	    return s.search(/^[A-Z][a-z]*$/) === 0;
	};

	// stringmethode om eerste letter om te zetten naar hoofdletter
	function capitalize(s) {
	    return s.charAt(0).toUpperCase() + s.slice(1);
	};

	// split madlib into fragments
    var fragments = madlib.split('_'), madlibs = [''];
    
    // generate list of suggested candidates for a given category
    function suggest(category, categories) {
    	
    	// fecth candidate suggestions from dictionary
        var candidates = categories[category.toLowerCase()];
        
        // format candidate suggestions according to category template
        if (isUpperCase(category)) {
            candidates = candidates.map(function(word) { return word.toUpperCase(); })
        } else if (isCapitalized(category)) {
        	candidates = candidates.map(function(word) { return capitalize(word); })
        }
        
        // return candidate suggestions
        return candidates;
        
    }
    
    // generate all possible madlibs
    for (var i = 0; i < Math.floor(fragments.length / 2); ++i) {
    	
        var newmadlibs = []
        var candidates = suggest(fragments[2*i+1], categories);
        
        for (var j = 0; j < madlibs.length; ++j) {
            for (k = 0; k < candidates.length; ++k) {
            	newmadlibs.push(madlibs[j] + fragments[2*i] + candidates[k]);
            }
        }
        
        madlibs = newmadlibs;
    }
    
    // append last fragment to all madlibs
    for (var j = 0; j < madlibs.length; ++j) {
    	
    	madlibs[j] = madlibs[j] + fragments[fragments.length - 1];
        
    }

    return madlibs.indexOf(generated) >= 0;
    
}

judge.config('auto-switch-context', false);
judge.config('switch-tab', 'MadLibs (1)');

// testgeval 0: dit testgeval is gegeven
judge.test("var madlib = new MadLibs();");

judge.test("madlib;", {'woordenschat':{}});

judge.test("madlib.leren('naam', 'god');");

judge.test("madlib.leren('ding', 'war');");

judge.test("madlib.leren('inwoners', 'Americans');");

judge.test("madlib.leren('discipline', 'geography');");

judge.test("madlib.woordenschat;", {'ding': ['war'], 'discipline': ['geography'], 'inwoners': ['americans'], 'naam': ['god']});

judge.test("madlib.suggereren('naam');", 'god');

judge.test("madlib.suggereren('NAAM');", 'GOD');

judge.test("madlib.suggereren('Naam');", 'God');

judge.test("madlib.suggereren('NaAm');", 'god');

judge.test(
	"madlib.invullen('_Naam_ created _ding_ so that _INWONERS_ would learn _DIScipline_.');", 
	'God created war so that AMERICANS would learn geography.',
	checkMadLibs,
	'_Naam_ created _ding_ so that _INWONERS_ would learn _DIScipline_.',
	{'ding': ['war'], 'discipline': ['geography'], 'inwoners': ['americans'], 'naam': ['god']}
);

judge.test("madlib.leren('naam', ['Mercator', 'Caesar']);");

judge.test("madlib.leren('ding', ['maps', 'coordinates']);");

judge.test("madlib.leren('inwoners', ['Belgians', 'Martians', 'Germans']);");

judge.test("madlib.leren('discipline', 'navigation');");

judge.test("madlib.leren('discipline', 'colonisation');");

judge.test("madlib.woordenschat;", {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']});

judge.test(
    "madlib.suggereren('naam');", 
    'god',
    checkMadLibs,
    '_naam_',
    {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']}
);

judge.test(
    "madlib.suggereren('NAAM');", 
    'GOD',
    checkMadLibs,
    '_NAAM_',
    {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']}
);

judge.test(
    "madlib.suggereren('Naam');", 
    'God',
    checkMadLibs,
    '_Naam_',
    {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']}
);

judge.test(
    "madlib.suggereren('NaAm');", 
    'god',
    checkMadLibs,
    '_NaAm_',
    {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']}
);

judge.test(
	"madlib.invullen('_Naam_ created _ding_ so that _INWONERS_ would learn _DIScipline_.');", 
	'Caesar created coordinates so that AMERICANS would learn geography.',
    checkMadLibs,
    '_Naam_ created _ding_ so that _INWONERS_ would learn _DIScipline_.',
    {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']}
);

judge.test(
    "madlib.invullen('_Naam_ created _ding_ so that _INWONERS_ would learn _DIScipline_.');", 
    'Caesar created coordinates so that AMERICANS would learn geography.',
    checkMadLibs,
    '_Naam_ created _ding_ so that _INWONERS_ would learn _DIScipline_.',
    {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']}
);

// controleert of methode invullen de woordenschat niet heeft gewijzigd
judge.test("madlib.woordenschat;", {'ding': ['war', 'maps', 'coordinates'], 'discipline': ['geography', 'navigation', 'colonisation'], 'inwoners': ['americans', 'belgians', 'martians', 'germans'], 'naam': ['god', 'mercator', 'caesar']});

judge.test("madlib.suggereren('land');", 'exception:MadLibsError: onbekende categorie');

judge.test("madlib.invullen('_INWONERS_ live in _Land_.');", 'exception:MadLibsError: onbekende categorie');

judge.config('switch-tab', 'MadLibs (2)');

judge.test("var madlib01 = new MadLibs();", undefined);

// testgeval 1
judge.test("madlib01.leren('skill', ['cars', 'programming', 'imagination', 'logic', 'mathematics', 'physics']);");

judge.test("madlib01.woordenschat", {'skill' : ['cars', 'programming', 'imagination', 'logic', 'mathematics', 'physics']});

judge.test(
	"madlib01.invullen('_Skill_ will get you from A to Z; _skill_ will get you everywhere.')", 
	'Cars will get you from A to Z; programming will get you everywhere.',
    checkMadLibs,
    '_Skill_ will get you from A to Z; _skill_ will get you everywhere.',
    {'skill' : ['cars', 'programming', 'imagination', 'logic', 'mathematics', 'physics']}
);

// testgeval 2
judge.config('switch-context');

judge.test("var madlib02 = new MadLibs();", undefined);

judge.test("madlib02.leren('adjective', ['clever', 'wise', 'skillful', 'witty', 'clumsy', 'stupid', 'dull', 'smart']);");

judge.test("madlib02.woordenschat;", {'adjective': ['clever', 'wise', 'skillful', 'witty', 'clumsy', 'stupid', 'dull', 'smart']});

judge.test(
	"madlib02.invullen('A _adjective_ person solves a problem. A _adjective_ person avoids it.')", 
	'A clumsy person solves a problem. A stupid person avoids it.',
    checkMadLibs,
    'A _adjective_ person solves a problem. A _adjective_ person avoids it.',
    {'adjective': ['clever', 'wise', 'skillful', 'witty', 'clumsy', 'stupid', 'dull', 'smart']}
);

// testgeval 3
judge.config('switch-context');

judge.test("var madlib03 = new MadLibs();", undefined);

judge.test("madlib03.leren('adjective', ['True', 'FALSE']);");

judge.test("madlib03.leren('NOUN', ['iDioT', 'GENIUS', 'Scientist']);");

judge.test("madlib03.leren('Pronoun', ['Nothing', 'Everything', 'nAdA', 'SoMeThInG']);");

judge.test("madlib03.woordenschat;", {'adjective': ['true', 'false'], 'noun': ['idiot', 'genius', 'scientist'], 'pronoun': ['nothing', 'everything', 'nada', 'something']});

judge.test(
	"madlib03.invullen('A _ADJECTIVE_ _noun_ admits that he knows _PROnoun_.')", 
	'A TRUE idiot admits that he knows something.',
    checkMadLibs,
    'A _ADJECTIVE_ _noun_ admits that he knows _PROnoun_.',
    {'adjective': ['true', 'false'], 'noun': ['idiot', 'genius', 'scientist'], 'pronoun': ['nothing', 'everything', 'nada', 'something']}
);

// testgeval 4
judge.config('switch-context');

judge.test("var madlib04 = new MadLibs();", undefined);

judge.test("madlib04.leren('country', ['belgium', 'malaysia', 'greenland', 'america']);");

judge.test("madlib04.leren('direction', ['right', 'left']);");

judge.test("madlib04.woordenschat;", {'country': ['belgium', 'malaysia', 'greenland', 'america'], 'direction': ['right', 'left']});

judge.test(
	"madlib04.invullen('How do you find _Country_? Turn _direction_ at _Country_.')", 
	'How do you find Greenland? Turn right at America.',
    checkMadLibs,
    'How do you find _Country_? Turn _direction_ at _Country_.',
    {'country': ['belgium', 'malaysia', 'greenland', 'america'], 'direction': ['right', 'left']}
);

// testgeval 5
judge.config('switch-context');

judge.test("var madlib05 = new MadLibs();", undefined);

judge.test("madlib05.leren('adjective', ['pleasant', 'nasty', 'clever', 'pretty']);");

judge.test("madlib05.leren('noun', ['girl', 'goat', 'cow', 'man']);");

judge.test("madlib05.leren('verb', ['work', 'eat', 'drive']);");

judge.test("madlib05.woordenschat;", {'adjective': ['pleasant', 'nasty', 'clever', 'pretty'], 'verb': ['work', 'eat', 'drive'], 'noun': ['girl', 'goat', 'cow', 'man']});

judge.test(
    "madlib05.invullen('Any _noun_ who can _verb_ safely while kissing a _adjective_ _noun_ is simply not giving the kiss the attention it deserves.')", 
    'Any goat who can eat safely while kissing a pretty cow is simply not giving the kiss the attention it deserves.',
    checkMadLibs,
    'Any _noun_ who can _verb_ safely while kissing a _adjective_ _noun_ is simply not giving the kiss the attention it deserves.',
    {'adjective': ['pleasant', 'nasty', 'clever', 'pretty'], 'verb': ['work', 'eat', 'drive'], 'noun': ['girl', 'goat', 'cow', 'man']}
);