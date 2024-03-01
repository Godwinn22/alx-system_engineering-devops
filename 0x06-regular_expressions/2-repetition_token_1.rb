#!/usr/bin/env ruby

arg = ARGV[0]

regex = /hb?tn/

occur = arg.scan(regex)

result = occur.join

puts result
