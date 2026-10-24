def sing():
    # your code here
    lyrics = []
    for i in range(99, 0, -1):
        beer = i
        if i == 1:
            minus_one = 'no more'
        else:
            minus_one = beer - 1
        lyrics.append(f"{beer} {'bottle' if i == 1 else 'bottles'} of beer on the wall, {beer} {'bottle' if i == 1 else 'bottles'} of beer.")
        lyrics.append(f"Take one down and pass it around, {minus_one} {'bottle' if i == 1 else 'bottles'} of beer on the wall.")
    lyrics.append(f"No more bottles of beer on the wall, no more bottles of beer.")
    lyrics.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return '\n'.join(lyrics)
print(sing())



