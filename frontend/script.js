const factText = document.getElementById("fact-text");
const factCategory = document.getElementById("fact-category");

async function getFact(category) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/facts/random/${category}`);
    if (!response.ok) throw new Error("No facts found in this category");

    const data = await response.json();
    factText.textContent = `"${data.content}"`;
    factCategory.textContent = `— ${data.category}`;
  } catch (error) {
    factText.textContent = "Oops! No facts available yet.";
    factCategory.textContent = "";
  }
}
