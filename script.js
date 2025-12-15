let c = "";
const p = document.createElement("p");
p.textContent = `${c}`;
const body = document.querySelector("body");
body.appendChild(p);
function para() {
    c=prompt("text?");
    if(c!=null)
        p.textContent = `${c}`;
}

const b = document.querySelector("button");
b.addEventListener("click", () => {
    para();
})