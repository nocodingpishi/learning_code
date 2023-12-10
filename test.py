import sys

print(sys.argv)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

my_dict = {
  "1": "hello",
  "2": "bye"
}
print(my_dict[arg2])