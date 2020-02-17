import axios from "axios";

const PATH = "/app/";

export default {
  async getAddress(addressId) {
    const result = await axios.get(`${PATH}address/${addressId}`);
    return result.data;
  },
  async getAddresses() {
    const result = await axios.get(`${PATH}address`);
    return result.data;
  },
  async postAddress(address) {
    const result = await axios.post(`${PATH}address`, address);
    return result.data;
  },
  async putAddress(addressId, address) {
    const result = await axios.put(`${PATH}address/${addressId}`, address);
    return result.data;
  },
  async deleteAddress(addressId) {
    const result = await axios.delete(`${PATH}address/${addressId}`);
    return result.data;
  }
};
