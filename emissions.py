#!/usr/bin/python3
import datetime, decimal, time
import argparse
from decimal import Decimal
import numpy as np

parser = argparse.ArgumentParser(description='Simple QRL emission program')
parser.add_argument('-r', action="store", dest="REPORT", default="blocks", help="Report type: blocks, daily")
parser.add_argument('-b', action="store", dest="BLOCK", default=1, help="Block to get", type=int)
parser.add_argument('-y', action="store", dest="YEARS", default=200, help="How many years to output. Default 200", type=int)
parser.add_argument('-c', action="store_true", dest="CUMULATIVE", default=False, help="Report as cumulative")

results = parser.parse_args()

REPORT = results.REPORT
CUMULATIVE = results.CUMULATIVE
BLOCK = results.BLOCK
YEARS = results.YEARS

# Coins to distribute
COINS = 40000000

def get_blocks(start_date, end_date):
  date_delta = end_date - start_date
  return divmod(date_delta.days * 86400 + date_delta.seconds, 60)[0]

def calc_coeff() -> Decimal:
    return Decimal(COINS).ln() / 105189120

# Blocks to distribute them in
START_DATE = datetime.datetime(2018, 4, 26, 0, 0, 0)  # Example start date.
END_DATE = datetime.datetime(2018 + YEARS, 4, 26, 0, 0, 0)    # Example end date.

TOTAL_BLOCKS = get_blocks(START_DATE, END_DATE)
# print("Total blocks between {} and {} = {}".format(START_DATE, END_DATE ,TOTAL_BLOCKS))

# Lambda
l = Decimal(np.log(COINS) / TOTAL_BLOCKS)
l = Decimal(1.664087503734056374552843909E-7)
l = Decimal(calc_coeff())

def remaining_emission(block_number) -> Decimal:
	coeff = Decimal(1.664087503734056374552843909E-7)
	return (COINS * decimal.Decimal(10 ** 9) * Decimal(-coeff * block_number).exp()).quantize(Decimal('1.'), rounding=decimal.ROUND_DOWN)

def block_reward(block_number) -> Decimal:
	if (block_number < 1938000):
		return remaining_emission(block_number - 1) - remaining_emission(block_number)
	else:
		return (remaining_emission(block_number - 1) - remaining_emission(block_number))*Decimal(0.4)
	

def sumblocks(start, end) -> Decimal:
	summit = 0

	# CSV header row
	print("block,emission")

	# CSV row
	for x in range(start,end):
		reward = block_reward(x+1)

		if CUMULATIVE is True:
			summit = Decimal(summit + block_reward(x+1))
			reward = summit

		print("{},{}".format(x+1,(Decimal(reward) * decimal.Decimal( 10 ** -9)).quantize(Decimal('0.000000001'), rounding=decimal.ROUND_HALF_DOWN)))

		pass

	# Sum total range
	# print("{}".format( (summit * decimal.Decimal(10 ** -9)).quantize(Decimal('0.000000001'), rounding=decimal.ROUND_HALF_DOWN) ))

def sumdays(start, end) -> Decimal:
	summit = 0
	sumall = 0
	day = 0
	date = datetime.datetime(2018, 6, 26)
	ndays = date + datetime.timedelta(seconds=3600*day)
	# print("Total emission {} to {}".format(start, end))

	# CSV header row
	print("day,emissions")

	for x in range(start,end):
		# block_reward = block_reward(x+1)
		summit = Decimal(summit + block_reward(x+1))
		# print("{},{}".format(x+1,(Decimal(block_reward(x+1)) * decimal.Decimal( 10 ** -9)).quantize(Decimal('0.000000001'), rounding=decimal.ROUND_HALF_DOWN)))

		if (x+1)%1440 == 0:
			day+=1

			if CUMULATIVE is True:
				sumall = Decimal(summit + sumall)
				summit = sumall

			ndays = date + datetime.timedelta(seconds=24*3600*day)
			print("{},{}".format(ndays.strftime('%Y-%m-%d'), (summit * decimal.Decimal(10 ** -9)).quantize(Decimal('0.000000001'), rounding=decimal.ROUND_HALF_DOWN) ))
			summit=0
			pass
		pass

def output_block(block_number) -> Decimal:
	reward = block_reward(block_number)

	print("{},{}".format(block_number,(Decimal(reward) * decimal.Decimal( 10 ** -9)).quantize(Decimal('0.000000001'), rounding=decimal.ROUND_HALF_DOWN)))


if REPORT=="blocks":
	sumblocks(0, TOTAL_BLOCKS)
elif REPORT=="daily":
	sumdays(0, TOTAL_BLOCKS)
elif REPORT=="block":
	output_block(BLOCK)
	pass