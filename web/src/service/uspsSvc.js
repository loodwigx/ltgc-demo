import axios from "axios";

const PATH = "/app/";

export default {
  async getCityState(zip) {
    try {
      const result = await axios.get(`${PATH}city-state/${zip}`);
      return result.data;
    } catch (err) {
      if (err.response.status === 400) return null;
      throw err;
    }
  },
  async getZip(address, city, state) {
    try {
      const result = await axios.get(`${PATH}zip/${btoa(address)}/${city}/${state}`);
      return result.data;
    } catch (err) {
      if (err.response.status === 400) return null;
      throw err;
    }
  }

};
