const s = readline();

function countCharactersOnce(input) {
  // Convert the input string to lowercase and remove whitespace
  const cleanedInput = input.toLowerCase().replace(/\s/g, '');

  // Initialize an empty object to store character counts
  const charCounts = {};

  // Count the occurrences of each character in the cleaned input
  for (const char of cleanedInput) {
    if (charCounts[char]) {
      charCounts[char]++;
    } else {
      charCounts[char] = 1;
    }
  }

  // Count the characters that occur exactly once
  let count = 0;
  for (const char in charCounts) {
    if (charCounts[char] === 1) {
      count++;
    }
  }

  return count;
}

console.log(countCharactersOnce(s));