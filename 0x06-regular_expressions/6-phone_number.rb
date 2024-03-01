#!/usr/bin/env ruby

arg = ARGV[0]

regex = /^[0-9]{10}$/

occur = arg.scan(regex)

result = occur.join

puts result
