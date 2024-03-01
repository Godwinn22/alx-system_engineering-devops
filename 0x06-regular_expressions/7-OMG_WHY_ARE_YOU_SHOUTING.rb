#!/usr/bin/env ruby

arg = ARGV[0]

regex = /[A-Z]/

occur = arg.scan(regex)

result = occur.join

puts result
