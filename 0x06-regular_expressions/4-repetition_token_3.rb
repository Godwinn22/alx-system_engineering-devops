#!/usr/bin/env ruby

arg = ARGV[0]

regex = /hbt{0,6}+n/

occur = arg.scan(regex)

result = occur.join

puts result
