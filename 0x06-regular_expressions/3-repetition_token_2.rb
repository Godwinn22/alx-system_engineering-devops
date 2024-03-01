#!/usr/bin/env ruby

arg = ARGV[0]

regex = /hbt{1,6}n/

occur = arg.scan(regex)

result = occur.join

puts result
