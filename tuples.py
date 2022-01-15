def getData(myTuple):
    nums = ()
    words = ()
    for t in myTuple:
        nums = nums + (t[0], )
        if t[1] not in words:
            words = words + (t[1], )
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)


tswift = ((2014, "Katy"),
          (2014, "Harry"),
          (2012, "Jake"),
          (2010, "Taylor"),
          (2008, "Joe"),
          (1998, "Hoe"))
(min_year, max_year, num_people) = getData(tswift)
print("From", min_year, "to", max_year,
      "Taylor Swift wrote songs about", num_people, "people!")

# this does not work as tuples are immuetable objects
# tswift[0] = (1345, "Xmas")
print(len(tswift))
print(tswift)
