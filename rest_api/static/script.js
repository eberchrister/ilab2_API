function expandTab(event) {
    // hide all content elements
    document.querySelectorAll(".content").forEach(content => content.style.display = "none");

    // remove active class from all tabs
    document.querySelectorAll(".tab").forEach(tab => tab.classList.remove("active"));

    // show the content of the selected tab and add active class to it
    const tabId = event.currentTarget.getAttribute("data-tab-target")
    document.querySelector(tabId).style.display = "block";
    event.currentTarget.classList.add("active");
}