document.addEventListener('DOMContentLoaded', () => {
  const recipes = [
    {
      title: 'Chocolate Cake',
      description: 'Delicious and rich chocolate cake.',
      image: 'images/chocolate-cake.jpg',
      category: 'Traditional'
    },
    {
      title: 'Fruit Cheesecake',
      description: 'Creamy cheesecake topped with fresh fruits.',
      image: 'images/fruit-cheesecake.jpg',
      category: 'Vegan'
    },
    {
      title: 'Brownies',
      description: 'Fudgy and gooey brownies.',
      image: 'images/brownies.jpg',
      category: 'Keto'
    },
    {
      title: 'Flan',
      description: 'Smooth and creamy flan.',
      image: 'images/flan.jpg',
      category: 'Traditional'
    }
  ];

  // Update featured recipe
  const featuredRecipe = recipes[0];
  document.getElementById('featured-img').src = featuredRecipe.image;
  document.getElementById('featured-title').textContent = featuredRecipe.title;
  document.getElementById('featured-description').textContent = featuredRecipe.description;
  document.querySelector('.featured-recipe').innerHTML += `<span class="categoria-label">${featuredRecipe.category}</span>`;

  // Update other recipes
  const otherRecipesContainer = document.getElementById('other-recipes');
  recipes.slice(1).forEach(recipe => {
    const article = document.createElement('article');
    article.innerHTML = `
      <img src="${recipe.image}" alt="${recipe.title}">
      <h3>${recipe.title}</h3>
      <span class="categoria-label">${recipe.category}</span>
    `;
    otherRecipesContainer.appendChild(article);
  });
});
