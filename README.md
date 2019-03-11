# Grammar based generating

## How it works?

Now it works as a binary operations generator without validating result.
The `grammar_generating.py` generates a `generator.py` python script according to `bin_grammar.g4`.
That generates the `generated` folder with test files named `testfile{NO}.js`, which contains the test cases.

## Usage

(Assuming that you are in the `grammar_based_generating` folder)

1. Run `grammar_generating.py` with arguments you need

    `./grammar_generating.py --starter-element STARTER_ELEMENT`

    required arguments:

   `--starter-element STARTER_ELEMENT` - Element of grammar to generate

    optional arguments:

    `--test-count TEST_COUNT` - Number of tests to generate

    `--seed SEED_NO` - Number of random seed

    `-q` - Hide debug information

2. Run `generator.py`

    `./generator.py`

    Your test files are now generated, here is an example output:

```JavaScript
(-6771397985115418)&(-8449399919839354),
(-1586649123906936)*(8892681406378659),
(7417463721077098)/(7755937561856221),
-6800068029534013,
8534292065816254,
8219444865984694,
427692400712034,
-4769654319939512,
(3916222245587407)*(-859047480842144),
-1761718781915079
```

 3. Run the generated test(s) with JerryScript

    (Engine location may be different)

    `./../jerryscript/build/bin/jerry ./generated/testfile1.js`

    At the moment you can only execute them separately, one by one.
