# QRL Tokenomics 

The goal of the QRL Tokenomics repository is to provide tools and datasets for end users to evaluate different tokenomics of QRL. This includes `macrotokencomics` and `microtokenomics`, but primarily deals with the latter.

If you're not looking to perform your own analysis into the tokenomics of QRL, and just want an overview, see the **additional references and notes section** at the end of this readme.

Currently consists of a base script `emissions.py`, along with a few output csv's in the data directory.

## emissions.py

Emissions can output the emission rate by days or blocks. The default is blocks.

```bash
usage: emissions.py [-h] [-r REPORT] [-b BLOCK] [-y YEARS] [-c]

Simple QRL emission program

optional arguments:
  -h, --help  show this help message and exit
  -r REPORT   Report type: blocks, daily
  -b BLOCK    Block to get
  -y YEARS    How many years to output. Default 200
  -c          Report as cumulative
```

### Examples

```bash
# Output daily rewards for 1 year
./emissions.py -r daily -y 1

# Output daily rewards for 5 years, cumulative
./emissions.py -r daily -y 5 -c

# Output block rewards, for 2 years, and ouput to csv
./emissions.py -r blocks -y 2 > blockrewards.2yr.csv

# Get rewards at blockheight 9000
./emissions.py -r block -b 9000
```

## Additional references and notes

Some `macrotokenomics` and `microtokenomics` are outlined at [https://theqrl.org/markets](https://theqrl.org/markets):

- Initial public supply: 52,000,000 Quanta
- Initial reserved supply: 13,000,000 Quanta (of which 8,000,000 Quanta reserved for distribution as determined by QRL Foundation)
- Initial total supply: 65,000,000 Quanta
- Emission 40,000,000 Quanta distributed via exponential decay emission schedule over approximately 200 years
- Eventual total supply: 105,000,000 Quanta
- Mining: Proof-of-Work, RandomX (Proof-of-Stake development underway)

The site [quantascan.io](https://quantascan.io) can also provide a lot of insight, such as:

- Average block size
- Average block time
- Block reward decay
- Transaction count/volume
- Transaction fee
- Total circulating Quanta
- Quanta distribution
- Rich list
- Number of wallets, and
- Stakers

## Known issues

- Due to dates being based off of a block time of 60 seconds, there ends up being a small drift due to real world conditions. In practice, that means the emission at an exact block height will be accurate, but daily emission rates should be seen more as estimates, both historically and in the future. Average drift seems to be about 1.75 days per year.