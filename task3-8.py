arr1 = [
    1, 2, 3,
    [
        "A", "B",
        [
            "string1", "string2", "string3"
        ]
    ]
]




#assignment: 03 print string3 from the arr1

print(arr1[3][2][2])

#assignment: 04 change string3 to "string4"

arr1[3][2][2]= "string4"
print(arr1)

# assignment: 05 remove "string4"

arr1[3][2].pop()
print(arr1)

# assignment: 06 add "string5" after string2

arr1[3][2].append('string5')
print(arr1)



arr2 = [3, 5, 1, 3, 5, 4, 10]

#assignment: 07 sort the arr2

arr2.sort()
print(arr2)


# assignment: 08 reverse the arr2

arr2.reverse()
print(arr2)



