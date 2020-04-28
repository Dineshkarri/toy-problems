// function to count the number of occurances of letter in the given word.
function countChar(word, letter) {
    if (letter.length > 1)
        return "only one letter allowed as second argument."

    let count = 0
    for (let i = 0; i < word.length; i++) {
        if (word[i] === letter) {
            count += 1
        }
    }
    return count
}

// function to count the number of b's in a given string.
function countBs(word) {
    return countChar(word, 'B')
}

// defining a string for testing.
const str = "bBbBB"

// printing the output of the function.
console.log(countBs(str))