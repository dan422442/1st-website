let c = 0

function para() {
    c++;
    const p = document.createElement("p");
    p.textContent = `${c}`;
    const body = document.querySelector("body");
    body.appendChild(p);
}

const b = document.querySelector("button");
b.addEventListener("click", () => {
    para()
})