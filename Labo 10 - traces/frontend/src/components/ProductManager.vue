<script setup lang="ts">
import { ref, onMounted, reactive } from "vue";

interface CreateProduct {
  name: string;
  description?: string;
  price: number;
}

interface Product {
  id: number;
  name: string;
  description?: string;
  price: number;
}

const products = ref<Product[]>([]);
const product = reactive<CreateProduct>({
  name: "",
  price: 0,
});

onMounted(() => {
  updateTable();
});

function updateTable() {
  fetch(`${import.meta.env.VITE_BACKEND_URL}/products/`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      products.value = data;
    });
}

function createProduct(product: CreateProduct) {
  fetch(`${import.meta.env.VITE_BACKEND_URL}/products/`, {
    method: "POST",
    body: JSON.stringify(product),
    headers: {
      "Content-Type": "application/json",
    },
  }).then(() => {
    product.name = "";
    product.description = undefined;
    product.price = 0;
    updateTable();
  });
}

function deleteProduct(id: number) {
  fetch(`${import.meta.env.VITE_BACKEND_URL}/products/${id}`, {
    method: "DELETE",
  }).then(() => {
    updateTable();
  });
}
</script>

<template>
  <div class="row">
    <div class="column">
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Description</th>
            <th>Price</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.description }}</td>
            <td>{{ product.price }}</td>
            <td>
              <button
                class="button button-outline"
                @click="deleteProduct(product.id)"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="column">
      <form>
        <fieldset>
          <label for="name">Name</label>
          <input v-model="product.name" type="text" id="name" />
          <label for="description">Description</label>
          <textarea v-model="product.description" id="description" />
          <label for="price">Price</label>
          <input v-model="product.price" type="number" id="price" />
          <input
            class="button-primary"
            type="submit"
            value="Create"
            @click.prevent="createProduct(product)"
          />
        </fieldset>
      </form>
    </div>
  </div>
</template>