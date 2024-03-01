#!/usr/bin/env ruby

arg = ARGV[0]

regex = /School/

occur = arg.scan(regex)

puts occur.join
