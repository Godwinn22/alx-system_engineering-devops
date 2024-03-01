#!/usr/bin/env ruby

arg = ARGV[0]

regex = /hbt+n/

occur = arg.scan(regex)

result = occur.join

puts result
