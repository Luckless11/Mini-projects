def hello(name)
  return "Hello #{name.chomp}!"
end

puts "Please enter your name:"

puts hello(gets)
