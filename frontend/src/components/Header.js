import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src="../../public/logo512.png"
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h5>
          <i>presents</i>
        </h5>
        <h1>Hi</h1>
      </div>
    );
  }
}

export default Header;