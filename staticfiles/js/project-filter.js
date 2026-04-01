document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".filter-btn");
    const items = document.querySelectorAll(".project-item");

    buttons.forEach(btn => {
        btn.addEventListener("click", function() {
            const cat = this.dataset.category;

            items.forEach(item => {
                const itemCat = item.dataset.category;
                if (cat === "all" || itemCat === cat) {
                    item.style.display = "block";
                } else {
                    item.style.display = "none";
                }
            });

            // Highlight active button
            buttons.forEach(b => b.classList.remove("active"));
            this.classList.add("active");
        });
    });
});