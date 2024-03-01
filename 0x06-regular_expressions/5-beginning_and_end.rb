#!/usr/bin/env ruby

arg = ARGV[0]

regex = /^h.{1}n$/

occur = arg.scan(regex)

result = occur.join

puts result
