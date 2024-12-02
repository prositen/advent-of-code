# Bash syntax

I never remember this from year to year so here are some reminders to myself:

## Arrays

* Initialize an array

```bash
my_array=("item 1" "item 2" "whatever") 
```

* Split a line into an array:

```bash
read -r -a my_array << "${line}"
```

* Append to array:

```bash
my_array+=("item")
```

* Array length

```bash
len_array="${#my_array[@]}"
```
 

* Iterate over elements. Array index `@` expands to all element.

```bash
for elem in "${my_array[@]}"; do
  ...
done
```

* Iterate over indixes: 


```bash
for elem in "${!my_array[@]}"; do
  ...
done
```

## Function calls

`echo` the return value instead of returning it and let the caller capture it  with the `$()` syntax

```bash
def fair_dice() {
  echo 4
}

echo $(fair_dice)
```

## Associative arrays

e.g. dictionaries


* Initialize & add values

```bash
declare -A my_dict
my_dict["fruit"]="banana"
```

* Check if key exists
```bash
if [[ -n "${my_dict["fruit"]}" ]] 
then
  echo "True"
else
  echo "False"
fi 
```

* Remove key
```bash
unset my_dict["fruit"]
```