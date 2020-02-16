import axios from "axios";

/**
 * This class is a wrapper around Axios so that we can change library without too much ceremony. It
 * also allows for the future support of things like stateful injection or request / response
 * interceptors.
 */
class Rest {
  /**
   * Create rest service.
   */
  constructor() {
    this.client = axios.create();
  }

  /**
   * performs an xhr using axios
   * @param {string} method - the request method or verb (get, post, etc)
   * @param {string} url - the path of the request, essentially everything after the host and port
   * @param {object} [data] - the data payload of the request, if any
   * @return {Promise} a promise that resolves (or rejects) based on the success of the request. The
   * full response payload will be returned.
   * @see https://github.com/axios/axios
   */
  async request(method, url, data) {
    return await this.client.request({method, url, data});
  }

  /**
   * Shorthand for performing a get request
   * @param {string} url - the path of the request, essentially everything after the host and port
   * @param {object} [params] - the query params for the request
   * @return {Promise} a promise that resolves (or rejects) based on the success of the request. The
   * full response payload will be returned.
   */
  async get(url, params) {
    return await this.client.get(url, {params});
  }
}

export default new Rest();
